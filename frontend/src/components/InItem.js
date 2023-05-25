import React, {useState, useEffect} from 'react';
import axios from 'axios';

function InItem({inItemId}) {
    const [isLoading, setIsLoading] = useState(true);
    const [inItem, setInItem] = useState();
    
    useEffect(() => {
	axios.get(`http://localhost:8000/in-items/${inItemId}`)
	    .then(function(response) {
		setIsLoading(false);
		setInItem(response.data);
	    });
    }, []);

    return (
	<div className='in-item'>{isLoading ? 'loading' : inItem.description}</div>
    );
};

export default InItem;
