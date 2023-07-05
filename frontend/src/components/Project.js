import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Project({projectId}) {
    const [data, setData] = useState(null);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
		axios.get(`http://localhost:8000/projects/${projectId}`)
		.then(response => {
			setIsLoading(false);
            setData(response.data);
	    });
    }, []);

    if (isLoading) return <p>loading...</p>;

    return (
        <>
            <h1>Project: {data.name}</h1>
            <div>created {data.created_at}</div>
            <div>status: {data.bucket}</div>
            <div>next step: {data.next_step}</div>
            <div>notes: {data.notes}</div>
        </>
    );
}

export default Project;
