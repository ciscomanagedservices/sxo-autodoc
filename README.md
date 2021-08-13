## SecureX Orchestrator AutoDoc: Template Git READMEs from Workflows

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/ciscomanagedservices/sxo-autodoc)

> **NOTE:** While this file will be copied over to any new repository templated off of this repository, its content will be overwritten when a new SecureX Orchestrator (SXO) workflow/atomic action is committed to the repository.

### Why does AutoDoc exist?

We know plenty of developers who use the description fields in their SXO workflows & atomic actions to describe what the workflow does, how to use it, what inputs to provide, what outputs to expect etc. Developers may also want to make this context available on their Git repositories with the README file for users to view prior to importing workflows/atomic actions into their SXO Org.

AutoDoc creates (and maintains) the README for developers based on a Jinja template, with the content defined in your SXO workflows/atomic actions.

---

### How do I use AutoDoc?

1. When creating a new repository to commit your SXO workflows/atomic actions to, select [ciscomanagedservices/sxo-autodoc](https://github.com/ciscomanagedservices/sxo-autodoc) as the repository template
2. This will initialize your new repository with the contents of this repository, i.e. with the `.github` folder and a `README.md` file
3. In your repository, create a new file called `template.md` within [/.github/templates/](/.github/templates/) and define your Jinja template. More on Jinja syntax [here](https://jinja.palletsprojects.com/en/3.0.x/templates/).
    1. For example, you may want to dynamically generate the name of the workflow with each commit, you'd do that by using `{{ workflow['name'] }}` in your template. Similarly, to template workflow descriptions, you'd use `{{ workflow['description'] }}`.
    2. Your template can have a mix of static content (text, images, GIFs etc.) and content that you'd like to be dynamically created from your workflow.
    3. A [sample template](/.github/templates/sample_template.md) is also included in the same directory for your reference.
4. No changes are required on SXO for AutoDoc to work. You'd setup the Git Endpoint for your repository on SXO and commit as you typically do.

💡 **Pro Tip**: Add `!#NODOC` to the description of your workflow before you commit to GitHub to tell AutoDoc not to run. When AutoDoc sees `!#NODOC` in a workflow's description, it does not update the README with that workflow's content.

---

### How does AutoDoc work?

AutoDoc uses [GitHub Actions](https://docs.github.com/en/actions) to trigger automation with every workflow commit you make. The automation looks at the Jinja template you've pre-defined and the workflow JSONs in the repository to dynamically generate the README content.

Please be aware of [pricing & usage limits](https://docs.github.com/en/actions/reference/usage-limits-billing-and-administration) associated to GitHub Actions.

---

### Known Limitations

1. [Changes to AutoDoc don't push to existing templated repositories](https://github.com/ciscomanagedservices/sxo-autodoc/issues/4)
2. [Need to add support for more keys that can be used in templates than just workflow name & description](https://github.com/ciscomanagedservices/sxo-autodoc/issues/2)

---

Contributors:

1. Aman Sardana (amasarda@cisco.com)
2. Anant Nambiar (ananambi@cisco.com)

Cisco CX Managed Services - Operate, August 2021
