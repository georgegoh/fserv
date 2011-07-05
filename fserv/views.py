import os
import json
import urllib
from pyramid.response import Response

def my_view(context, request):
    return {'project':request.method + request.path_info + str(context)}


def home_view(context, request):
    if context.downloadable:
      res = Response(content_type="application/octet-stream", app_iter=context.payload)
      return res

    if request.method=="POST":
        func = request.params.get('func')
        if func=='list':
            return site_view(context, request)
        elif func=='upload':
            return upload(context, request)

    return {'store_name': context.storename,
            'http_method': request.method,
            'url': request.url.strip('/'),
            'parent_url': os.path.split(request.url.strip('/'))[0],
            'path': request.path_info,
            'curdir': context.curdir,
            'directories': context.dirs,
            'files': context.files,
            'downloadable': context.downloadable,
            'freespace': context.freespace,
            'error': context.error!='',
            'error_msg': context.error}


def upload(context, request):
    dest_path = os.path.join(context.basedir, urllib.unquote(request.params['dir']), request.params['file'].filename)
    print 'Destination path: ', dest_path
    bytes_read = 0
    with open(dest_path, 'w') as f:
        buf = request.params['file'].file.read(1024)
        while len(buf) > 0:
            f.write(buf)
            bytes_read += len(buf)
            buf = request.params['file'].file.read(1024)

    print bytes_read
    res = Response(content_type="text/plain", body=json.dumps({'status': 'ok', 'size': bytes_read}))
    return res


def site_view(context, request):
    r=['<ul class="jqueryFileTree" style="display: none;">']
    try:
        r=['<ul class="jqueryFileTree" style="display: none;">']

        requested_dir = urllib.unquote(request.params['dir'].strip('/')
        d=requested_dir
        if not d.startswith(context.basedir):
          d=os.path.join(context.basedir, requested_dir)
        print "basedir: ", context.basedir
        print "listing directory: ", d
        for f in os.listdir(d):
            ff=os.path.join(d,f)
            rel=os.path.join(requested_dir,f)
            if os.path.isdir(ff):
                r.append('<li class="directory collapsed"><a href="#" rel="%s/">%s</a></li>' % (rel,f))
            else:
                e=os.path.splitext(f)[1][1:] # get .ext and remove dot
                r.append('<li class="file ext_%s"><a href="#" rel="%s">%s</a></li>' % (e,rel,f))
        r.append('</ul>')
    except Exception,e:
        r.append('Could not load directory: %s' % str(e))
    r.append('</ul>')
    return Response(body=''.join(r))
