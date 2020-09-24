import requests
from django.shortcuts import render, redirect
from django.conf import settings
from isodate import parse_duration

def home(request):
    return render(request, 'search/index.html')

def index(request):
    videos = []
    if request.method == 'POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
            'part': 'snippet',
            'q': request.POST['search'],
            'key': settings.YOUTUBE_DATA_API_KEY,
            'type': 'video',
            'maxResults' : 9,
        }

        r = requests.get(search_url, params=search_params)

        results = r.json()['items']
        
        video_ids = []

        for result in results:
            video_ids.append(result['id']['videoId'])
        
        if request.POST['submit'] == 'lucky':
            return redirect(f'https://www.youtube.com/watch?v={ video_ids[0] }')


        video_params = {
            'key': settings.YOUTUBE_DATA_API_KEY,
            'part': 'snippet, contentDetails',
            'id': ','.join(video_ids),
            'maxResults	': 9
        }

        r = requests.get(video_url, params=video_params)
        
        results= r.json()['items']

        for result in results:
            video_date = {
                'title': result['snippet']['title'],
                'id': result['id'],
                'url': f'https://www.youtube.com/watch?v={ result["id"] }',
                'duration': int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60) ,
                'thumbnail': result['snippet']['thumbnails']['high']['url']
            }

            videos.append(video_date)

    context = {
        'videos': videos
    }

    return render(request, 'search/search_result.html', context)

def SearchFormView(request):
    rq = request
    print(rq)
    sort1 = request.GET.get('name')
  
    # queryset=Channel.objects.all()
    # for row in queryset.values_list():
    #     print(row)
    
    # print(sort1)
    # print(sort2)
    # queryset = Channel.objects.all()
    # for row in queryset.values_list():
    #     print (row)
    Channel.objects.all()
    obs = Channel.objects.filter(food_name=name).only( "video_title", "video_link")
    
    context = {'obs':obs}
    print(obs)
    return render(request,'mylist/searchresult.html' , context)