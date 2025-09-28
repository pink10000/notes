# Notes Collection

Welcome to my notes! 

---
# System Overview: Astro Site + Quartz Notes

This setup integrates a collection of notes managed with Quartz into a subdirectory (`/notes/`) of a main website built with Astro. Both parts are deployed automatically via GitHub Actions to GitHub Pages.

## Repositories

1.  **Notes Repository**
    * https://github.com/pink10000/notes
    * Contains the source Markdown notes (`.md` files) organized in folders located in the repository **root**.
    * Contains the `quartz` subfolder with the Quartz library files, `package.json`, and configuration.
    * **`quartz/quartz.config.ts`:**
        * Configured with `baseUrl: "pink10000.github.io"` so generated links work correctly under the `/notes/` path.
        * Uses `ignorePatterns` to prevent Quartz from processing non-content files/folders found in the root (like `.git`, `.github`, `README.md`, the `quartz` folder itself, etc.).
    * **`quartz/content/` Directory:** Contains a git submodule that pulls from upstream  (created using `ln -s ../<folder> <folder>` etc.) pointing to the actual notes folders and the `index.md` file located in the repository root (`../`). These symlinks are committed to Git.
    * **GitHub Actions (`.github/workflows/deploy.yml`):**
        * Triggers on push to the `main` branch.
        * Checks out code, sets up Node, installs/builds Quartz (primarily verifying build integrity).
        * Uses `peter-evans/repository-dispatch` to send a `deploy-notes` event trigger to the Astro repository, authenticating with a `DISPATCH_PAT` secret (Personal Access Token with `repo` scope).
2. **Quartz Fork**
	- https://github.com/pink10000/quartz-site 
	- Forked from [here](https://github.com/jackyzha0/quartz). 
	- Contains a git submodule in `content/` that pulls from upstream when triggered by a push in the `notes` repository
3.  **Astro Site Repository**
    * https://github.com/pink10000/pink10000.github.io
    * Contains the source code for the main Astro website.
    * Includes a `.nojekyll` file in the root to prevent default GitHub Pages Jekyll processing.
    * **GitHub Pages Settings:** Configured to deploy using the **`GitHub Actions`** source.
    * **GitHub Actions (`.github/workflows/deploy-astro.yml`):**
        * Triggers on push to `main` OR on receiving the `repository_dispatch` event (type `deploy-notes`) from the `notes` repository.
        * **Deploy Job:**
            1.  Uses `actions/deploy-pages` to take the `github-pages` artifact uploaded by the `build` job and deploy it to the GitHub Pages environment.

## Local Preview (Notes Repository)
1. Clone the [quartz fork](https://github.com/pink10000/quartz-site ) 
2. Check if you need to pull from upstream for the git submodule(s) in `content`
3. Run `npx quartz build --serve`

Check [this](https://quartz.jzhao.xyz/build) if not clear.

## Result

* The main Astro website is available at `https://pink10000.github.io/`.
* The published Quartz notes are available under `https://pink10000.github.io/notes/`.
* Updates pushed to the `main` branch of the Notes repository automatically trigger the Quartz fork pull + rebuild and deployment of both the notes and the main Astro site.

---

*Last updated: {{ date }}*