from django.core.management.base import BaseCommand
import json
import os
from dash_backend.models import Report
class Command(BaseCommand):
    help = "This terminal command import jsondata into SQLlite"

    def handle(self,*args, **kwargs):
        json_file = open(str(os.getcwd()) + "\jsondata.json", encoding='utf-8')
        data = json.load(json_file)
        for iterator in data:
            Report.objects.create(
                end_year = iterator['end_year'],
                intensity = iterator['intensity'],
                sector = iterator['sector'],
                topic = iterator['topic'],
                insight = iterator['insight'],
                url = iterator['url'],
                region = iterator['region'],
                start_year = iterator['start_year'],
                impact = iterator['impact'],
                added = iterator['added'],
                published = iterator['published'],
                country = iterator['country'],
                relevance = iterator['relevance'],
                pestle = iterator['pestle'],
                source = iterator['source'],
                title = iterator['title'],
                likelihood = iterator['likelihood']
            )
        json_file.close()
        self.stdout.write(self.style.SUCCESS("Data Imported"))