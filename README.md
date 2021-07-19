## SecureX Orchestrator AutoDoc: Template Git READMEs from Workflows

> **NOTE:** While this file will be copied over to any new repository templated off of this repository, its content will be overwritten when a new SecureX Orchestrator (SXO) workflow/atomic action is committed to the repository.

### Why does this thing exist?

We know plenty of developers who use the description fields in their SXO workflows & atomic actions to describe what the workflow does, how to use it, what inputs to provide, what outputs to expect etc. Developers may also want to make this context available on their Git repositories with the README file for users to view prior to importing workflows/atomic actions into their SXO Org.

AutoDoc creates (and maintains) the README for developers based on a Jinja template, with the content defined in your SXO workflows/atomic actions.

### How do I use this thing?

1. When creating a new repository to commit your SXO workflows/atomic actions to, select [ciscomanagedservices/sxo-autodoc](https://github.com/ciscomanagedservices/sxo-autodoc) as the repository template
2. This will initialize your new repository with the contents of this repository, i.e. with the `.github` folder and a `README.md` file
3. In your repository, head over to the [template.md](/.github/templates/) file within `/.github/templates/` and define your Jinja template. More on Jinja syntax [here](https://jinja.palletsprojects.com/en/3.0.x/templates/).
    1. For example, you may want to dynamically generate the name of the workflow with each commit, you'd do that by using `{{ workflow['name'] }}` in your template. Similarly, to template workflow descriptions, you'd use `{{ workflow['description'] }}`.
    2. Your template can have a mix of static content (text, images, GIFs etc.) and content that you'd like to be dynamically created from your workflow.
    3. A [sample template](/.github/templates/) is also included in the same directory for your reference.
4. No changes are required on SXO for AutoDoc to work. You'd setup the Git Endpoint for your repository on SXO and commit as you typically do.

### How does this thing work?

AutoDoc uses [GitHub Actions](https://docs.github.com/en/actions) to trigger automation with every workflow commit you make. AutoDoc looks at the Jinja template you've defined and the workflow JSONs in the repository to dynamically generate the README content.

Please be aware of [usage limits](https://docs.github.com/en/actions/reference/usage-limits-billing-and-administration) associated to using GitHub Actions.

---

Contributors:

1. Aman Sardana (amasarda@cisco.com)
2. Anant Nambiar (ananambi@cisco.com)

Cisco CX Managed Services - Operate, July 2021
