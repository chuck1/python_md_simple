
import os
import markdown

for root, dirs, files in os.walk('src'):
    #print root
    #print dirs
    #print files
    for f in files:
        h,t = os.path.splitext(f)
        if t == '.md':
            src = os.path.join(root, f)
            dst = os.path.join('build', root, f)
            print src
            print dst
            
            with open(src, 'r') as fd:
                raw = fd.read()

            html = markdown.markdown(raw)

            try:
                os.makedirs(os.path.dirname(dst))
            except OSError:
                pass

            with open(dst, 'w') as fd:
                fd.write(html)


