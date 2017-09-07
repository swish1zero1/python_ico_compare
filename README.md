# Crypto Coin ICO Compare

## To install

Clone the repository into a local folder

```
git clone https://github.com/swish1zero1/python_ico_compare.git
cd python_ico_compare
```

Create a virtual environment called `venv` in the base project folder. (If you don't have virtualenv, install using `pip install virtualenv`, more info [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/#next-steps))

```
virtualenv venv
```

Start the virtual environment. From the base project folder run:

```
source venv/bin/activate
```

Install the required packages

```
pip install -r requirements.txt
```

## To run

```
python3 program.py
```

## Notes

When adding new packages, you can update the `requirements.txt` by executing: 
```
pip freeze > requirements.txt
```