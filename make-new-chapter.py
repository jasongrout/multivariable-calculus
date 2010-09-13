#!/usr/bin/env python

TEMPLATE="Chapter-Template"
project_name='multivariable-calculus'


if __name__ == '__main__':

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--chapter-num", dest="chapter_num", type=int,
                      help="number for chapter", metavar="DIR")
    parser.add_option("--chapter-title", dest="chapter_title",
                      help="title for chapter")
    parser.add_option("--chapter-name", dest="chapter_name",
                      help="name for chapter (i.e., filename)")

    (options, args) = parser.parse_args()
    chapter_title=options.chapter_title
    chapter_dir='%02d'%options.chapter_num+'-'+options.chapter_name
    chapter_name=options.chapter_name
    
    import os
    import shutil
    from string import Template
    class latex_template(Template):
        delimiter="\REPLACE"

    os.mkdir(chapter_dir)
    for filename in os.listdir(TEMPLATE):
        in_filepath=os.path.join(TEMPLATE,filename)
        out_filepath=os.path.join(chapter_dir,chapter_name+'-'+filename)
        with open(in_filepath) as f:
            raw=latex_template(f.read())
        raw.delimiter="\REPLACE"
        with open(out_filepath,'w') as f:
            f.write(raw.substitute(chapter_title=chapter_title, 
                                   chapter_name=chapter_name, 
                                   chapter_dir=chapter_dir,
                                   project_name=project_name))

              
    
