berlinunited.github.io
======================
First install the pip dependencies  
`python -m pip install -r requirements.txt`

## Local Development
To run the website locally run:
`mkdocs serve`

## Deployment
To deploy the website to github pages run:
`mkdocs gh-deploy`

This will modify the branch `gh-pages` and push it, which in turn we trigger github to show the new website. Sometimes
this can take a couple of minutes.

---
## Notes
- Example for building own plugins: https://docs.abinit.org/theory/noncollinear/ This could be used to add bibtex support

