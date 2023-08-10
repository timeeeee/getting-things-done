import React, { useEffect, useState } from 'react';
import { useLoaderData } from 'react-router-dom';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';


export async function projectLoader(data) {
    const projectId = data.params.projectId;
    const response = await axios.get(`http://localhost:8000/projects/${projectId}`);
    const project = response.data;
    return { project };
}


function Project({projectId}) {
    const { project } = useLoaderData();

    const [ isEditing, setIsEditing ] = useState(false);

    const handleEdit = () => {
        setIsEditing(true);
    }

    const handleSave = (event) => {
        event.preventDefault();

        setIsEditing(false);
        
        const putData = {
            name: event.target.name.value,
            notes: event.target.notes.value,
            bucket: project.bucket,
            next_step: event.target.next_step.value,
        };

        axios.put(`http://localhost:8000/projects/${projectId}`, putData)
        .then(response => {
            setData(response.data);
        });
    }

    if (isEditing) {
        return (
             <form method='put' onSubmit={handleSave}>
                <label>
                    Name:
                    <input type='text' name='name' defaultValue={project.name} />
                </label>
                
                <label>
                    Next step:
                    <input type='text' name='next_step' defaultValue={project.next_step} />
                </label>
                
                <label>
                    Notes:
                    <textarea name='notes' defaultValue={project.notes} />
                </label>
                
                <button type='submit'>Save</button>
            </form>
        );
    } else {
        return (
            <>
                <h1>Project: {project.name}</h1>
                <div>created {project.created_at}</div>
                <div>status: {project.bucket}</div>
                <div>next step: {project.next_step}</div>
                <div>notes: <ReactMarkdown>{project.notes}</ReactMarkdown></div>
                <button onClick={handleEdit}>edit</button>
            </>
        );
    }
}

export default Project;
