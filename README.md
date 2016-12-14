
\_template
==========

The `_template` repository provides a set of templates for use with `cookiecutter`
(https://cookiecutter.readthedocs.io/en/latest/index.html).


usage
=====

Create a new repository in the current working directory:

```
cookiecutter git@git.internal.getwellnetwork.com:plcdev/_template.git
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


branches
========

Different types of templates (e.g. "a python library", "a dbus service") are
provided by the branches in this repository.

The `master` branch serves as a blank, mostly empty repository template that
provides only our standard debian packaging boilerplate. It's a good starting
point if you want to create a new template from (nearly) scratch.

