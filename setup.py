from setuptools import setup
setup(name="WikiPageScrapper",
      version="0.1",
      author="Vishesh Bansal",
      author_email="vishesh.bansal2020@vitstudent.ac.in",
      url="https://github.com/VisheshBansal/Wikipedia-scraper",
      packages=['scrapper'],
      install_requires=[
          "beautifulsoup4==4.9.3",
          "bs4==0.0.1",
          "certifi==2020.12.5",
          "chardet==4.0.0",
          "idna==2.10",
          "requests==2.25.1",
          "soupsieve==2.1",
          "urllib3==1.26.2"],
      short_description = "Wikipedia Webpage Scraper",
      long_description="Scraps content from wikipedia pages and stores in an object",
      long_description_content_type='text/markdown',
      )