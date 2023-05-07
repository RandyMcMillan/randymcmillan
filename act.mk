#NOTE: using -C for container context
#The action is run on the submodule .github as an example
act-github-alpine:docker-start## 	run act in .github
	@export $(cat ~/GH_TOKEN.txt) && act -C $(PWD)/.github -vr -W $(PWD)/.github/.github/workflows/alpine.yml