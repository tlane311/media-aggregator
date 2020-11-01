from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

posts = [
    {
    'title': 'The First Astronauts Step Foot on Mars',
    'age': '1 day ago',
    'content_is_text': False,
    'content': 'INSERT IMAGE HERE',
    'user': 'NASA (Official)',
    'likes': '2 million'
    },
    {
    'title': 'This Dog is Smarter than her Owner',
    'age': '2 hours ago',
    'content_is_text': False,
    'content': 'INSERT IMAGE HERE',
    'user': 'not-a-content-farm-i-swear',
    'likes': '20 million'
    },
    {
    'title': 'Amazing Sports Play by Midwestern Sportsball Team just Happened',
    'age': '16 hours ago',
    'content_is_text': True,
    'content': 'INSERT IMAGE HERE',
    'text': 'LET\'S GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!',
    'user': 'thiccFemurTX',
    'likes': '520 thousand'
    },
    {
    'title': 'please like this post, I failed my math test today and my cat is cute',
    'age': '7 hours ago',
    'content_is_text': False,
    'content': 'INSERT IMAGE HERE',
    'user': 'send_me_pictures_of_CATS',
    'likes': '23 thousand'
    }
]

single_post = {
    'title': 'The First Astronauts Step Foot on Mars',
    'age': '1 day ago',
    'content_is_text': False,
    'content': 'INSERT IMAGE HERE',
    'user': 'NASA (Official)',
    'likes': '2 million',
    'comments': [
        {
            'user': 'angry_user',
            'likes': 123,
            'content': 'asdagkjhasd;fjhasdfkja'
        },
        {
            'user': 'furious_user',
            'likes': 123,
            'content': 'asdagkjhasd;fjhasdfkja'
        },
        {
            'user': 'belligerent_user',
            'likes': 123,
            'content': 'asdagkjhasd;fjhasdfkja'
        }
    ]
}

def home(request):
    context = {
        'posts': posts+posts+posts
    }
    return render(request, 'posts/home.html', context)


def individual_community(request, community_id):
    context = {
        'community_name': "my first community",
        'posts': posts+posts+posts
    }
    return render(request, 'posts/individual_community.html', context)

def individual_post(request,community_id, post_id):
    context ={
        "individual_post":single_post
    }
    return render(request, 'posts/individual_post.html', context)

def user(request, user_id):
    return HttpResponse("User: "+user_id)

def communities(request):
    context ={
        "communities":[
            {
                'title': 'tech',
                'age': '6 years ago',
                'description': 'a community for those who like tech',
                'users': '6k'
            },
            {
                'title': 'CuteAnimals',
                'age': '600 years ago',
                'description': 'only the cutest animals',
                'users': '600k'
            },
            {
                'title': 'WhatShouldIWatchNext',
                'age': '10 months ago',
                'description': 'come here for tv/movie recommendations',
                'users': '36k'
            },
            {
                'title': 'tech',
                'age': '6 years ago',
                'description': 'a community for those who like tech',
                'users': '6k'
            },
            {
                'title': 'CuteAnimals',
                'age': '600 years ago',
                'description': 'only the cutest animals',
                'users': '600k'
            },
            {
                'title': 'WhatShouldIWatchNext',
                'age': '10 months ago',
                'description': 'come here for tv/movie recommendations',
                'users': '36k'
            },
            {
                'title': 'tech',
                'age': '6 years ago',
                'description': 'a community for those who like tech',
                'users': '6k'
            },
            {
                'title': 'CuteAnimals',
                'age': '600 years ago',
                'description': 'only the cutest animals',
                'users': '600k'
            },
            {
                'title': 'WhatShouldIWatchNext',
                'age': '10 months ago',
                'description': 'come here for tv/movie recommendations',
                'users': '36k'
            },
            {
                'title': 'tech',
                'age': '6 years ago',
                'description': 'a community for those who like tech',
                'users': '6k'
            },
            {
                'title': 'CuteAnimals',
                'age': '600 years ago',
                'description': 'only the cutest animals',
                'users': '600k'
            },
            {
                'title': 'WhatShouldIWatchNext',
                'age': '10 months ago',
                'description': 'come here for tv/movie recommendations',
                'users': '36k'
            },
        ]
    }
    return render(request, 'posts/communities.html', context)

def community(request):
    return redirect('communities')

def error(request):
    return HttpResponse('Page not found', 404)