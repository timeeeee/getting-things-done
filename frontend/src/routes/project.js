import React, { useEffect, useState } from 'react';
import { useFetcher } from 'react-router-dom';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';


// get projectId as argument instead?
export async function projectLoader(data) {
    const projectId = data.params.projectId;
    const response = await axios.get(`http://localhost:8000/projects/${projectId}`);
    const project = response.data;
    return { project };
}


export async function updateProjectAction({ params, request }) {
	const formData = await request.formData();
    console.log("form data is...");
    console.log(formData);
	
	const response = await axios.put(
		`http://localhost:8000/projects/${formData.get("id")}`,
		{
            name: formData.get("name"),
            next_step: formData.get("next_step"),
            notes: formData.get("notes"),
            bucket: formData.get("bucket"),
        }
	);
	const project = await response.data;
	return { project };
}


function Project() {
    const [ isEditing, setIsEditing ] = useState(false);
    // const [ isSaving, setIsSaving ] = useState(false);
    const fetcher = useFetcher();    

    useEffect(() => {
        if (fetcher.state === 'idle' && !fetcher.data) {
            // fetcher.load(`/projects/${projectId}`)
            fetcher.load();
        }

		if (fetcher.state === 'submitting') {
			setIsEditing(false);
		}
	}, [fetcher])

    if (!fetcher.data) return <p>loading...</p>;

    const project = fetcher.data.project;

    if (isEditing) {
        return (
             <fetcher.Form method='post' action='/projects/update'>
                <input type='hidden' name='id' value={project.id} />
                <input type='hidden' name='bucket' value={project.bucket} />

                <div><label>
                    Name:
                    <input type='text' name='name' defaultValue={project.name} />
                </label></div>
                
                <label>
                    Next step:
                    <input type='text' name='next_step' defaultValue={project.next_step} />
                </label>
                
                <label>
                    Notes:
                    <textarea name='notes' defaultValue={project.notes} />
                </label>
                
                <button type='submit'>Save</button>
            </fetcher.Form>
        );
    } else {
        return (
            <>
                <h1>Project: {project.name}</h1>
                <div>created {project.created_at}</div>
                <div>status: {project.bucket}</div>
                <div>next step: {project.next_step}</div>
                <div>notes: <ReactMarkdown>{project.notes}</ReactMarkdown></div>
                <button onClick={() => setIsEditing(true)}>edit</button>
            </>
        );
    }
}

export default Project;
