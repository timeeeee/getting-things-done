import React, { useEffect } from 'react';
import { Link, useLoaderData } from 'react-router-dom';
import axios from 'axios';


export async function projectListLoader() {
    const response = await axios.get('http://localhost:8000/projects/');
    const projects = response.data;
    return { projects };
}


const ProjectList = () => {
    const { projects } = useLoaderData();

    useEffect(() => {
        // console.log(projects);
    }, [projects])

    return (
        <ul>
            {projects.map(project => <li key='{project.id}'><Link to={`/projects/${project.id}`}>{project.name}</Link></li>)}
        </ul>
    )
}

export default ProjectList;