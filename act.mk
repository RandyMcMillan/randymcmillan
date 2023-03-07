act-autogen-alpine:## 	run act in .github
	@pushd .github && export $(cat ~/GH_TOKEN.txt) && act -vbr -W .github/workflows/autogen_alpine.yml && popd