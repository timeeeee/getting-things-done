import React, {useState, useEffect} from 'react';
import axios from 'axios';

import InItem from './InItem';

function InItemList() {
    const [isLoading, setIsLoading] = useState(true);
    const [inItems, setInItems] = useState([]);

    useEffect(() => {
	axios.get('http://localhost:8000/in-items')
	    .then(response => {
		setIsLoading(false);
		setInItems(response.data);
	    });
    }, []);

    if (isLoading) return <p>loading...</p>;
    
    return (
	<ul>
	    {inItems.map(item => <InItem description={item.description} />)}
	</ul>
    );
}

export default InItemList;
