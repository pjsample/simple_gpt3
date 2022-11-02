# simple_gpt3
A lightweight script for calling GPT-3 in your terminal.


### Getting it to work
```
pip install openai
git clone git@github.com:pjsample/simple_gpt3.git

cd simple_gpt3
chmod +x gpt.py
cp gpt.py gpt

export PATH=$PATH:$PWD

export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

### Example
`$gpt "Write a bash script that will read the lines from "myinputs.txt" and then execute the python script "myscript.py" using the text of each line as the value for the "--input" parameter."

```
#!/bin/bash

while read line
do
    python myscript.py --input "$line"
done < myinputs.txt
```
