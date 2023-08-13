from django import views
from django.shortcuts import render

class Index(views.View):
    def get(self, request):
        return render(request, 'index.html', {})        

class About(views.View):
    def get(self, request):
        data = {
            'staff' : [
                {'name' : 'Walter White', 'position' : 'Chief Executive Officer', 'image' : 'assets/img/team/team-1.jpg'},
                {'name' : 'Sarah Jhonson', 'position' : 'Product Manager', 'image' : 'assets/img/team/team-2.jpg'},
                {'name' : 'William Anderson', 'position' : 'CTO', 'image' : 'assets/img/team/team-3.jpg'},
                {'name' : 'Amanda Jepson', 'position' : 'Accountant', 'image' : 'assets/img/team/team-4.jpg'},
            ]
        }
        return render(request, 'about.html', data)

class Blog(views.View):
    def get(self, request):
        return render(request, 'blog.html', {})

class Contact(views.View):
    def get(self, request):
        data = {
            'location' : 'A108 Adam Street, York, NY 535022',
            'email' : 'info@example.com',
            'phone' : '+1 5589 55488 55',
            }
        return render(request, 'contact.html', data)

class Services(views.View):
    def get(self, request):
        data = {
            'services' : [
                {'title' : 'Lorem Ipsum',
                 'description' : 'Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident',
                 'icon' : 'bi bi-briefcase',
                 'color' : '#f57813'},
                
                {'title' : 'Dolor Sitema',
                 'description' : 'Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata',
                 'icon' : 'bi bi-card-checklist',
                 'color' : '#15a04a'},
                
                {'title' : 'Sed ut perspiciatis',
                 'description' : 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur',
                 'icon' : 'bi bi-briefcase',
                 'color' : '#d90769'},
                
                {'title' : 'Magni Dolores',
                 'description' : 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum',
                 'icon' : 'bi bi-binoculars',
                 'color' : '#15bfbc'},
                
                {'title' : 'Nemo Enim',
                 'description' : 'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque',
                 'icon' : 'bi bi-brightness-high',
                 'color' : '#f5cf13'},
                
                {'title' : 'Eiusmod Tempor',
                 'description' : 'Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi',
                 'icon' : 'bi bi-calendar4-week',
                 'color' : '#1335f5'},
                
                
            ]
        }
        return render(request, 'services.html', data)

