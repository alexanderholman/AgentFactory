<!-- Written by Alexander Holman 19/08/2019 -->
<!--
This file should contain a step by step guide on how to install, update and remove the software, along with any 
prerequisites for each step should they exist. It is written to be used with most internal projects, but as per the 
other documents feel free to adapt it to fit your needs, adding, modifying and removing as necessary.
-->

# Installation

## Prerequisites 
<!-- List of a conditions that need to be met prior to installation, including os requirements, dependancies, etc -->
<!-- EXAMPLE START -->
* Git for cloning the repository
* A GitHub account for using the templates
<!--  EXAMPLE END -->

## From scratch
<!-- Step-by-step guide on how to install -->
<!-- EXAMPLE START -->
Use this repository as a GitHub template to create a new repository with the same structure.

**Option 1: Use GitHub's Template Feature (Recommended)**
1. Visit the [AgentFactory repository](https://github.com/alexanderholman/AgentFactory)
2. Click the green "Use this template" button
3. Select "Create a new repository"
4. Fill in your new repository details and click "Create repository"

**Option 2: Clone for Local Development**
If you need to work with the templates locally:
```bash
git clone https://github.com/alexanderholman/AgentFactory.git
```
<!--  EXAMPLE END -->

## Updating
<!-- Step-by-step guide on how to update -->
<!-- EXAMPLE START -->
**Note:** Template repositories are designed to be a starting point. Once you create a repository from this template, it becomes independent. Most users will customize their documentation and don't need to pull updates from the template.

However, if you want to incorporate specific updates from AgentFactory:

**Option 1: Manual Update (Advanced)**
1. Add AgentFactory as a remote:
```bash
git remote add template https://github.com/alexanderholman/AgentFactory.git
git fetch template
```
2. Carefully merge specific files or changes as needed (note: this may conflict with your customizations):
```bash
git checkout template/main -- path/to/file
```

**Option 2: Fresh Start**
If you haven't customized the templates much, you can create a new repository from the updated template and migrate your custom content.
<!--  EXAMPLE END -->

## Removal and how-to uninstall
<!-- Step-by-step guide on how to remove the software -->
<!-- EXAMPLE START -->
If you created a repository from this template and want to remove it:

**On GitHub:**
1. Go to your repository Settings
2. Scroll to the bottom "Danger Zone" section
3. Click "Delete this repository"

**Locally:**
Simply remove the directory from your system:
```bash
rm -rf your-repository-name
```
<!--  EXAMPLE END -->