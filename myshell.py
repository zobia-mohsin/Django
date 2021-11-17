import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','learning_log.settings')

import django
django.setup()

from MainApp.models import Topic, Entry

#select * in sql = dot notation in python
topics = Topic.objects.all()

for topic in topics:
    print(topic.id, topic) #since we defined the __Str__ method, we can use the topic to get topic.text

t = Topic.objects.get(id=1)

print(t.text)
print(t.date_added)

entries = t.entry_set.all()

for entry in entries:
    print(entry)