import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';


function Project({projectId}) {
    const [data, setData] = useState(null);
    const [isLoading, setIsLoading] = useState(true);
    const [isEditing, setIsEditing] = useState(false);

    useEffect(() => {
		axios.get(`http://localhost:8000/projects/${projectId}`)
		.then(response => {
			setIsLoading(false);
            setData(response.data);
	    });
    }, []);

    const handleEdit = () => {
        setIsEditing(true);
    }

    const handleSave = (event) => {
        event.preventDefault();

        setIsEditing(false);
        setIsLoading(true);
        
        const putData = {
            name: event.target.name.value,
            notes: event.target.notes.value,
            bucket: data.bucket,
            next_step: event.target.next_step.value,
        };

        axios.put(`http://localhost:8000/projects/${projectId}`, putData)
        .then(response => {
            setIsLoading(false);
            setData(response.data);
        });
    }

    if (isLoading) return <p>loading...</p>;

    if (isEditing) {
        return (
             <form method='put' onSubmit={handleSave}>
                <label>
                    Name:
                    <input type='text' name='name' defaultValue={data.name} />
                </label>
                
                <label>
                    Next step:
                    <input type='text' name='next_step' defaultValue={data.next_step} />
                </label>
                
                <label>
                    Notes:
                    <textarea name='notes' defaultValue={data.notes} />
                </label>
                
                <button type='submit'>Save</button>
            </form>
        );
    } else {
        return (
            <>
                <h1>Project: {data.name}</h1>
                <div>created {data.created_at}</div>
                <div>status: {data.bucket}</div>
                <div>next step: {data.next_step}</div>
                <div>notes: <ReactMarkdown>{data.notes}</ReactMarkdown></div>
                <button onClick={handleEdit}>edit</button>
            </>
        );
    }
}

export default Project;
