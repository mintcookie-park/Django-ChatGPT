from django.shortcuts import render
from django.views import View
from dotenv import load_dotenv
import openai
import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ConversationSerializer
from .models import ChatingRoom, Message
from rest_framework.authtoken.models import Token


load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


class ChatView(APIView):
    def get(self, request, format=None):
        loginToken = request.GET.get('token')
        room_name = request.GET.get('room')

        token = Token.objects.get(key=loginToken)
        user = token.user

        room = ChatingRoom.objects.get(name=room_name, user=user)

        prev_conversations = Message.objects.filter(
            ChatingRoom=room).order_by('created_at')
        if prev_conversations:
            conversations = []
            for elem in prev_conversations:
                conversations.append(
                    {'prompt': elem.prompt, 'response': elem.response})
        else:
            conversations = []
        request.session['conversations'] = conversations
        print(prev_conversations)
        print(request.session.get('conversations', []))
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        loginToken = request.data.get('token')
        token = Token.objects.get(key=loginToken)
        user = token.user
        room_name = request.data.get('room')
        room = ChatingRoom.objects.get(name=room_name, user=user)
        prompt = request.data.get('prompt')

        if prompt:

            session_conversations = request.session.get('conversations', [])
            condition = '''Assistant will conduct a role play in English.
                        Assistant should always answer in english, even when requested to answer in a different language.
                        Assistant will respond with one sentence at a time, taking turns in the conversation and waiting for a response before replying.
                        Assistant is a 1 year old female Persian cat owned by the user.
                        The assistant's name is Bori.
                        At the end of each sentence, add 'meow.'
                        The assistant introduces itself in the first sentence by stating its name, age, and species.'''

            previous_conversations = "\n".join(
                [f"User: {c['prompt']}\nAI: {c['response']}" for c in session_conversations])
            prompt_with_previous = f"{previous_conversations}\nUser: {prompt}\nAI:"

            model_engine = "text-davinci-003"
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=prompt_with_previous,
                max_tokens=1024,
                n=5,
                stop=None,
                temperature=0.5,
            )
            response = completions.choices[0].text.strip()

            msg = Message.objects.create(
                prompt=prompt, response=response, ChatingRoom=room)

            conversation = {'prompt': prompt, 'response': response}
            session_conversations.append(conversation)
            request.session['conversations'] = session_conversations
            request.session.modified = True

        conversations = request.session.get('conversations', [])
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChatListView(APIView):
    pass
