
# claramatos.github.io

This is the source code for my [personal website](https://claramatos.github.io/).

Built with [Pelican](https://getpelican.com/) and deployed using Github Pages.

## Features
- Static site generated with Pelican
- Custom theme and templates
- Content written in Markdown
- Automated deployment to GitHub Pages

## Getting Started

### 1. Clone the repository
```sh
git clone https://github.com/claramatos/claramatos.github.io.git
cd claramatos.github.io
```


### 2. Create a virtual environment
```sh
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies with uv
```sh
pip install uv
uv pip install -r requirements.uv.txt
```

### 4. Build the site
```sh
make html
```

### 5. Serve locally
```sh
make serve
```

### 6. Publish to GitHub Pages
```sh
make github
```

## License
[MIT](LICENSE)