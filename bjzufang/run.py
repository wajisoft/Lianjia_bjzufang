from scrapy import cmdline

name = 'lianjia'
cmd = 'scrapy crawl {}'.format(name)
cmdline.execute(cmd.split())
