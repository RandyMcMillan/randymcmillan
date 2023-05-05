act-autogen-alpine:docker-start## 	run act in .github
	@pushd .github && export $(cat ~/GH_TOKEN.txt) && act -vr -W .github/workflows/autogen_alpine.yml && popd