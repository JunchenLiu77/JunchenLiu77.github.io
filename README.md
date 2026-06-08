This is the source code for Junchen Liu's academic website, which is built upon the structure and design of [Jon Barron&#39;s website](https://jonbarron.info/).

## Repository Structure

- `index.html`: main personal website.
- `sections/`: homepage section partials.
- `templates/`: HTML shell used to generate `index.html`.
- `scripts/build_index.py`: rebuilds `index.html` from the template and section partials.
- `assets/css/`: shared site styles.
- `assets/cv/`: CV and resume files.
- `assets/images/profile/`: profile images.
- `assets/images/papers/`: publication thumbnails.
- `projects/`: standalone project pages and their local assets.

To edit the homepage, update the matching file in `sections/`, then run:

```bash
python3 scripts/build_index.py
```
