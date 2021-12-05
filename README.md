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
this can take a couple of minutes. Do not change the gh-pages branch manually!

If you cloned the repo via ssh and use a shh key that is not named id_rsa or is not at the standard location `~/.ssh` you have to specify your settings in a config file inside `~/.ssh`. Otherwise the push of the new changes can't work.
```
Host github.com
   HostName github.com
   IdentityFile ~/.ssh/my_private_key_name
   IdentitiesOnly yes
```

---
## Notes
- Example for building own plugins: https://docs.abinit.org/theory/noncollinear/ This could be used to add bibtex support
- Used theme: https://squidfunk.github.io/mkdocs-material/
- Docs for mkdocs: https://www.mkdocs.org/
