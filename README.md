# Shortify - URL Shortener

Shortify is a URL shortener project that provides a simple and convenient way to shorten long URLs. It utilizes Astro.js for the frontend, which is deployed on an AWS S3 bucket. The backend is implemented using a Python Lambda function deployed on AWS, and the redirect feature is built with React and react-router-dom, deployed on Vercel.

## Features

- Shorten long URLs to create compact and shareable links.
- Redirect users to the original URL when they access the shortened link.
- Easy deployment and hosting using AWS S3, AWS Lambda, and Vercel.

## Environment Variables

The following environment variables need to be set:

## Frontend
PUBLIC_API_URL: This variable represents the public API URL used by the frontend.
PUBLIC_GET_URL: This variable represents the public URL for retrieving data in the frontend.
PUBLIC_RESULT_URL: This variable represents the public URL for displaying results in the frontend.
PUBLIC_ERROR_URL: This variable represents the public URL for displaying errors in the frontend.

## Backend
DOMAIN_URL: This variable represents the domain URL of the backend server.
DB_URL: This variable represents the URL of the database used by the backend.
DB_PASSWORD: This variable represents the password for accessing the database.
DB_USER: This variable represents the username for accessing the database.

## Redirect
VITE_FETCH_URL: This variable represents the URL used for fetching data in the redirect project.
VITE_ERROR_URL: This variable represents the URL for displaying errors in the redirect project.
VITE_HOME_URL: This variable represents the URL for the home page of the redirect project.

## Deployment

Shortify can be deployed using the following services:

- Frontend (Astro.js): AWS S3 Bucket
  - Build the Astro.js project: `npm run build`
  - Upload the generated files to an S3 bucket.
  - Configure the bucket for static website hosting and set the appropriate permissions.
- Backend (Python Lambda Function): AWS Lambda
  - Package the Lambda function code and dependencies into a ZIP file.
  - Create a Lambda function in the AWS Management Console.
  - Upload the ZIP file and configure the necessary triggers and permissions.
- Redirect Feature (React and react-router-dom): Vercel
  - Create a Vercel account and connect it to your repository.
  - Configure the necessary build settings and environment variables.
  - Deploy the project to Vercel.

Make sure to set the required environment variables in the deployment platforms as mentioned in the "Environment Variables" section.

## Acknowledgements

Shortify utilizes the following open-source libraries and frameworks:

- Astro.js - [Link](https://astro.build)
- React - [Link](https://reactjs.org)
- react-router-dom - [Link](https://reactrouter.com)
- AWS S3 - [Link](https://aws.amazon.com/s3)
- AWS Lambda - [Link](https://aws.amazon.com/lambda)
- Vercel - [Link](https://vercel.com)

# Folder Tree

## Frontend
```
astro-frontend
├── .env
├── .env.local
├── astro.config.mjs
├── package-lock.json
├── package.json
├── public
│   ├── link.svg
│   └── styles
│       ├── error.css
│       ├── index.css
│       └── loading.css
├── README.md
├── src
│   ├── components
│   │   └── Card.astro
│   ├── env.d.ts
│   ├── layouts
│   │   └── Layout.astro
│   └── pages
│       ├── error.astro
│       ├── index.astro
│       └── results.astro
└── tsconfig.json
```

## Backend

```
backend
├── .env
├── get-original-url
│   ├── constants.py
│   ├── DB_connection.py
│   └── lambda_function.py
├── get_urls
│   ├── constants.py
│   ├── DB_connection.py
│   └── lambda_function.py
└── shorten_url
    ├── code_generator.py
    ├── constants.py
    ├── lambda_function.py
    └── url_validator.py
```

## Redirect Feature
```
react-redirect
├── .env
├── .eslintrc.cjs
├── .gitignore
├── index.html
├── link.svg
├── package-lock.json
├── package.json
├── public
│   └── vite.svg
├── README.md
├── src
│   ├── assets
│   ├── css
│   │   ├── error.css
│   │   └── loader.css
│   ├── index.css
│   ├── main.jsx
│   └── routes
│       ├── Error.jsx
│       └── Loader.jsx
├── vercel.json
└── vite.config.js
```

