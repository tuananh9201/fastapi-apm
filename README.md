## Requirements

- FastApi
- Postgres
- ...

## QuickStart

1. create conda env or python env

- using conda:
  create and activate env

```
conda create -n helpdesk python=3.8
conda activate helpdesk
```

2. install packages

```
cd backend && pip install -r requirements.txt
```

3. Run backend
   cd to backend folder

```
uvicorn app.main:app --reload
```

4. start dependencies...
