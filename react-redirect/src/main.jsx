import React from 'react';
import ReactDOM from 'react-dom/client';
import Loader from "./routes/Loader.jsx";
import Error from "./routes/Error.jsx";
import './index.css'

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Error />,
    errorElement: <Error />,
  },
  {
    path: "/:id",
    element: <Loader />,
  },
]);


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
