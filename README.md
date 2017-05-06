
\_template
==========

The `_template` repository provides a set of templates for use with `cookiecutter`
(https://cookiecutter.readthedocs.io/en/latest/index.html).


code review notes
=================

Some extra notes about code reviewing this project:

1.  this project doesn't follow the tagging release workflow that the rest of our projects do
1.  feature branching is possible, so that part of the review workflow is the same except
    that changes are "live" after pushing the merge into master, not a tag built by jenkins
1.  work with the developer to determine which other branches a feature should also be merged
    into, considering that the branching model in this project represents template inheritance


usage
=====

Create a new repository under the current working directory:

```
cookiecutter git@git.internal.getwellnetwork.com:plcdev/_template.git
```

selecting a template
--------------------

Different types of templates (e.g. "a python library", "a dbus service") are
provided by the branches in this repository.

You can select different branches with cookiecutter's `-c` or `--checkout`
option.

```
cookiecutter git@git.internal.getwellnetwork.com:plcdev/_template.git -c python-library
```

configuration
-------------

To avoid typing out this full repository URL every time you want to use
cookiecutter, you can create a `.cookiecutterrc` file in your home directory
that includes aliases for commonly used template repositories. For example, here
is mine which allows me to just refer to this repository as `_template`.

```yaml
abbreviations:
    _template: git@git.internal.getwellnetwork.com:plcdev/_template.git
```

Now I can just run it like this:

```
cookiecutter _template
```

and selecting which template to use now looks like this:

```
cookiecutter _template -c python-library
```

operating on an existing directory
----------------------------------

By default, `cookiecutter` will refuse to operate on a project directory that
already exists. To do so, you'll need to use the `-f` flag. Ths is useful, for
example, when initially populating a new (empty) repository.

```
git clone git@git.internal.getwellnetwork.com:plcdev/gwn-empty-repo.git
cookiecutter -f _template
```

Note that you'll still have to fill in the `repository_name` field manually
when prompted.


master
======

The `master` branch serves as a blank, mostly empty repository template that
provides only our standard debian packaging boilerplate. It's a good starting
point if you want to create a new template from (nearly) scratch.

This branch provides:

* debian packaging boilerplate; the following make targets will work:
	* `apt-silo`
	* `tag`
	* `deb`
	* `installnow`
	* `graph`

