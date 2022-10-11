## CREATE

```sh
git init

git checkout -b main
```

## SET email & username

```sh
git config user.email "<EMAIL_ID>@users.noreply.github.com"
git config user.name "unsco"
```

## INITIAL Commit

```sh
git status -vv  # // Quick check...

git add .

git commit -am "Initial commit."

git status -vv  # // Quick check...
```

## Set REPO

```sh
git remote add dummy https://github.com/uncsco/dummy
```

## PUSH...

```sh
git push dummy

fatal: The current branch main has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream dummy main
```

```sh
git push --set-upstream dummy main
```

### Info - List of branches

```
git branch --list --verbose
```

## Cycle - Add, Commit, Push

```sh
git add    ...
git commit ...
git push   ...
```

## ANOTHER repo

- Add a repo (named `dummy_2`)

```sh
git remote add dummy_2 https://gitlab.com/______-PUB/dummy_2
```

- Push to repo `dummy_2`

```sh
git push dummy_2
```

### Info - List of repos

```sh
git remote --verbose
```
