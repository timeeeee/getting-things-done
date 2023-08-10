import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

import Root from './routes/root';
import InItemList, { inItemListLoader, createInItemAction, updateInItemAction } from './routes/inItems';
import ProjectList, { projectListLoader } from './routes/projects';
import Project, { projectLoader } from './routes/project';

import ErrorPage from './error-page';


const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <ErrorPage />,
    // loader: rootLoader,
    children: [
      {
        path: "/in-items/",
        element: <InItemList />,
        loader: inItemListLoader,
        children: [
          {
            path: "/in-items/create/",
            action: createInItemAction,
          },
          {
            path: "/in-items/update/",
            action: updateInItemAction,
          }
        ]
      },
      {
        path: "/projects/",
        loader: projectListLoader,
        element: <ProjectList />,
      },
      {
        path: "/projects/:projectId",
        loader: projectLoader,
        element: <Project />,
      }
    ],
  },
]);


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
