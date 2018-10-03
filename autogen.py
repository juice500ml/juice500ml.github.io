import collections
import datetime
import glob
import re

series = collections.defaultdict(lambda:[])
for pdf in glob.glob('./assets/pdfs/*'):
    name = pdf.split('/')[-1]
    if re.fullmatch('\w+(-\w+)+\-\d\d\.pdf$', name):
        series[name[:-7]].append(name)

for v in series.values():
    v.sort()

blueprints = dict()
for post in glob.glob('./_posts/*.markdown'):
    for name, pdfs in series.items():
        if pdfs[0][:-3] in post:
            blueprints[name] = post

new_files = collections.defaultdict(lambda:[])
for name, pdfs in series.items():
    for pdf in pdfs:
        found = False
        for post in glob.glob('./_posts/*.markdown'):
            if pdf[:-3] in post:
                found = True
        if not found:
            new_files[name].append(pdf)

for name, pdfs in new_files.items():
    for pdf in pdfs:
        with open(blueprints[name]) as f:
            blueprint = f.readlines()
        idx = pdf[-6:-4]
        time = datetime.datetime.today() + datetime.timedelta(minutes=int(idx))
        post_filename = time.strftime('%Y-%m-%d-') + pdf[:-4] + '.markdown'

        blueprint[2] = blueprint[2].replace('01', idx)
        blueprint[3] = time.strftime('date:   %Y-%m-%d %H:%M:%S\n')
        for num, line in enumerate(blueprint):
            blueprint[num] = line.replace(series[name][0], pdf)

        with open('_posts/' + post_filename, 'w') as f:
            for line in blueprint:
                f.write(line)

