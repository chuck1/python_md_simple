#!/usr/bin/env python

import markdown
import jinja2
import os
import sys

def get_source():
        md_files = []
        for root, dirs, files in os.walk('.'):
                for f in files:
                        h,t = os.path.splitext(f)
                        if t == '.md':
                                p = os.path.join(root,f)
                                p = os.path.normpath(p)
                                md_files.append(p)
        return md_files

def get_html():
		l = []
		for root, dirs, files in os.walk('build'):
				for f in files:
						h,t = os.path.splitext(f)
						if t == '.html':
								p = os.path.join(root,f)
								p = os.path.normpath(p)
								l.append(p)
		return l
		
def listize(path):
        l = []
        h = path
        while True:
                h,t = os.path.split(h)

                l.insert(0, t)

                if not t: break
                if not h: break
        return l        

def sitemap_insert(m, p, p0):

        if not p:
                return
        
        try:
                m0 = m[1][p[0]]
        except:
                m[1][p[0]] = (p0, {})
                m0 = m[1][p[0]]
        
        sitemap_insert(m0, p[1:], p0)

def sitemap(files):
        m = ([],{})
        for f in files:
			f = listize(f)
			f = f[1:]
			
			sitemap_insert(m, f, f)

        return m

def sm_open_default(pre, test, p0):
        return '{0}{1}'.format(pre, test)

def sm_open_html(pre, test, p0):
        #print 'p0',p0
        if p0:
                p = os.path.join(*p0)
                h0,t0 = os.path.splitext(test)
                h,t = os.path.splitext(p)
                if t0 == '.html':
                        return '{0}<ul><li><a href="{1}">{2}</a></li>'.format(pre, h+'.html', h0)

        return '{0}<ul><li>{1}</li>'.format(pre, test)

def sitemap_html(m):
        return sitemap_print(
                m,
                [],
                '',
                sm_open_html,
                '{0}</ul>')


def sitemap_print(m, l = [], pre = '', func_open = sm_open_default, fmt_close = None):
        
        for k,v in m[1].items():
                if func_open:
                        l.append(func_open(pre, k, m[0]))
                l = sitemap_print(v, l, pre+' ', func_open, fmt_close)
                if fmt_close:
                        l.append(fmt_close.format(pre, k))

        return l

def process(src, temp):

	#print src
	
	h,t = os.path.splitext(src)
	dst = os.path.join('build', h+'.html')
	
	#print dst
	
	dir = os.path.dirname(dst)
	
	try:
		os.makedirs(dir)
	except OSError:
		pass
	
	with open(src, 'r') as f:
		raw = f.read()
	
	md_out = markdown.markdown(raw)
	
	html = temp.render(html = md_out)
	
	with open(dst, 'w') as f:
		f.write(html)

#########################################################

os.chdir('P:\\doc')
print os.getcwd()

md_files = get_source()
html_files = get_html()

with open('template.html','r') as f:
	temp_raw = f.read()

temp = jinja2.Template(temp_raw)


for f in md_files:
	process(f, temp)

#m = sitemap(md_files)
m = sitemap(html_files)

body = sitemap_html(m)
body = '\n'.join(body)

html = temp.render(html = body)

with open('build/map.html', 'w') as f:
        f.write(html)

#l = sitemap_print(m)
#print '\n'.join(l)



