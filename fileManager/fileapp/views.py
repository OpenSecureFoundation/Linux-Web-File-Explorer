

from django.shortcuts import render


def home_view(request):
    # ── Données fictives pour la vue ──────────────────────────
    current_path = '/home/cridavec/public_html'

    folders = [
        {'name': '.cagefs',       'size': '4 KB',  'modified': 'Dec 9, 2025, 12:41 PM',  'permissions': '0771'},
        {'name': '.caldav',       'size': '4 KB',  'modified': 'Jan 5, 2026, 4:12 PM',   'permissions': '0755'},
        {'name': '.cl.selector',  'size': '4 KB',  'modified': 'Jan 24, 2026, 4:56 PM',  'permissions': '0755'},
        {'name': '.clwpos',       'size': '4 KB',  'modified': 'Dec 9, 2025, 12:39 PM',  'permissions': '0700'},
        {'name': '.cpanel',       'size': '4 KB',  'modified': 'Today, 11:20 AM',         'permissions': '0700'},
        {'name': '.htpasswds',    'size': '4 KB',  'modified': 'Dec 9, 2025, 12:39 PM',  'permissions': '0755'},
        {'name': '.koality',      'size': '4 KB',  'modified': 'Dec 9, 2025, 5:31 PM',   'permissions': '0755'},
        {'name': '.softaculous',  'size': '4 KB',  'modified': 'Dec 9, 2025, 5:31 PM',   'permissions': '0711'},
        {'name': '.spamassassin', 'size': '4 KB',  'modified': 'Dec 9, 2025, 12:39 PM',  'permissions': '0700'},
        {'name': '.trash',        'size': '4 KB',  'modified': 'Today, 6:27 AM',          'permissions': '0700'},
        {'name': 'app',           'size': '4 KB',  'modified': 'Jan 10, 2026, 9:00 AM',  'permissions': '0755'},
        {'name': 'assets',        'size': '4 KB',  'modified': 'Jan 12, 2026, 2:15 PM',  'permissions': '0755'},
        {'name': 'cache',         'size': '4 KB',  'modified': 'Today, 8:00 AM',          'permissions': '0700'},
        {'name': 'etc',           'size': '4 KB',  'modified': 'Jan 25, 2026, 8:05 AM',  'permissions': '0750'},
        {'name': 'logs',          'size': '4 KB',  'modified': 'Today, 10:12 AM',         'permissions': '0700'},
        {'name': 'mail',          'size': '4 KB',  'modified': 'Jan 5, 2026, 4:12 PM',   'permissions': '0751'},
        {'name': 'public_ftp',    'size': '4 KB',  'modified': 'Dec 9, 2025, 12:39 PM',  'permissions': '0750'},
        {'name': 'public_html',   'size': '4 KB',  'modified': 'Jan 6, 2026, 12:28 PM',  'permissions': '0755'},
        {'name': 'ssl',           'size': '4 KB',  'modified': 'Dec 9, 2025, 2:23 PM',   'permissions': '0755'},
        {'name': 'uploads',       'size': '4 KB',  'modified': 'Today, 3:45 PM',          'permissions': '0755'},
    ]

    files = [
        {'name': '.htaccess',       'size': '1.2 KB', 'modified': 'Jan 20, 2026, 9:10 AM',  'type': 'text/plain',       'permissions': '0644', 'ext': 'txt'},
        {'name': 'composer.json',   'size': '3.4 KB', 'modified': 'Dec 15, 2025, 11:00 AM', 'type': 'application/json', 'permissions': '0644', 'ext': 'json'},
        {'name': 'composer.lock',   'size': '120 KB', 'modified': 'Dec 15, 2025, 11:02 AM', 'type': 'application/json', 'permissions': '0644', 'ext': 'json'},
        {'name': 'index.php',       'size': '5.8 KB', 'modified': 'Jan 18, 2026, 3:22 PM',  'type': 'text/x-php',       'permissions': '0644', 'ext': 'php'},
        {'name': 'README.md',       'size': '2.1 KB', 'modified': 'Dec 10, 2025, 8:00 AM',  'type': 'text/markdown',    'permissions': '0644', 'ext': 'md'},
        {'name': 'robots.txt',      'size': '0.5 KB', 'modified': 'Dec 9, 2025, 12:40 PM',  'type': 'text/plain',       'permissions': '0644', 'ext': 'txt'},
        {'name': 'sitemap.xml',     'size': '18 KB',  'modified': 'Jan 22, 2026, 7:30 AM',  'type': 'text/xml',         'permissions': '0644', 'ext': 'xml'},
        {'name': 'style.css',       'size': '42 KB',  'modified': 'Jan 19, 2026, 5:00 PM',  'type': 'text/css',         'permissions': '0644', 'ext': 'css'},
        {'name': 'wp-config.php',   'size': '3.2 KB', 'modified': 'Dec 12, 2025, 2:00 PM',  'type': 'text/x-php',       'permissions': '0400', 'ext': 'php'},
        {'name': 'error_log',       'size': '88 KB',  'modified': 'Today, 10:11 AM',         'type': 'text/plain',       'permissions': '0600', 'ext': 'log'},
        {'name': 'favicon.ico',     'size': '4 KB',   'modified': 'Dec 9, 2025, 12:40 PM',  'type': 'image/x-icon',     'permissions': '0644', 'ext': 'ico'},
        {'name': 'screenshot.png',  'size': '256 KB', 'modified': 'Jan 14, 2026, 10:05 AM', 'type': 'image/png',        'permissions': '0644', 'ext': 'png'},
    ]

    # Arborescence sidebar
    sidebar_tree = [
        {
            'name': '(/home/cridavec)',
            'path': '/home/cridavec',
            'is_root': True,
            'children': [
                {'name': '.cagefs',      'path': '/home/cridavec/.cagefs',      'children': []},
                {'name': '.caldav',      'path': '/home/cridavec/.caldav',      'children': []},
                {'name': '.cpanel',      'path': '/home/cridavec/.cpanel',      'children': [
                    {'name': '.htpasswds', 'path': '/home/cridavec/.cpanel/.htpasswds', 'children': []},
                    {'name': '.koality',   'path': '/home/cridavec/.cpanel/.koality',   'children': []},
                ]},
                {'name': 'etc',          'path': '/home/cridavec/etc',          'children': []},
                {'name': 'logs',         'path': '/home/cridavec/logs',         'children': []},
                {'name': 'mail',         'path': '/home/cridavec/mail',         'children': []},
                {'name': 'public_ftp',   'path': '/home/cridavec/public_ftp',   'children': []},
                {'name': 'public_html',  'path': '/home/cridavec/public_html',  'is_current': True, 'children': [
                    {'name': '.well-known', 'path': '/home/cridavec/public_html/.well-known', 'children': []},
                    {'name': 'app',         'path': '/home/cridavec/public_html/app',         'children': [
                        {'name': 'Actions',    'path': '/home/cridavec/public_html/app/Actions',    'children': []},
                        {'name': 'Console',    'path': '/home/cridavec/public_html/app/Console',    'children': [
                            {'name': 'Exceptions', 'path': '/home/cridavec/public_html/app/Console/Exceptions', 'children': []},
                            {'name': 'Exports',    'path': '/home/cridavec/public_html/app/Console/Exports',    'children': []},
                        ]},
                        {'name': 'Http',       'path': '/home/cridavec/public_html/app/Http',       'children': []},
                    ]},
                    {'name': 'assets',      'path': '/home/cridavec/public_html/assets',      'children': []},
                    {'name': 'uploads',     'path': '/home/cridavec/public_html/uploads',     'children': []},
                ]},
                {'name': 'ssl',          'path': '/home/cridavec/ssl',          'children': []},
            ]
        }
    ]

    context = {
        'current_path': current_path,
        'folders': folders,
        'files': files,
        'sidebar_tree': sidebar_tree,
    }
    return render(request, 'base.html', context)