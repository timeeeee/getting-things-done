import React, {useState, useEffect, useRef} from 'react';
import axios from 'axios';

function InItem({description, id}) {
    return <li className='in-item' key={id}>{description}</li>;
}

function InItemList() {
    const [isLoading, setIsLoading] = useState(true);
    const [inItems, setInItems] = useState([]);
	const [isInputDisabled, setIsInputDisabled] = useState(false);
	const [uploadError, setUploadError] = useState();

	const formRef = useRef(null);
	const descriptionInputRef = useRef(null);

	// load the items on first render
    useEffect(() => {
		axios.get('http://localhost:8000/in-items')
		.then(response => {
			setIsLoading(false);
			setInItems(response.data);
	    });
    }, []);

	// focus every render
	useEffect(() => {
		const element = descriptionInputRef.current;
		if (element !== null) element.focus();
	}, [inItems]);

	const handleSubmit = (event) => {
		event.preventDefault();
		setIsInputDisabled(true);
		axios.post('http://localhost:8000/in-items', {'description': event.target.description.value})
		.then(response => {
			setIsInputDisabled(true);
			setInItems([...inItems, response.data]);
			formRef.current.reset();
		})
		.catch(error => {
			setUploadError(error);
		})
		.finally(() => {
			setIsInputDisabled(false);
		});
	}

    if (isLoading) return <p>loading...</p>;
    
    return (
	<>
		<ul>
			{inItems.map(item => <InItem description={item.description} key={item.id} />)}
		</ul>

		<form onSubmit={handleSubmit} ref={formRef}>
			<h2>Add an item</h2>
			<input type='text' name='description' disabled={isInputDisabled} ref={descriptionInputRef} />
			<input type='submit' disabled={isInputDisabled} value='submit' />
			{(uploadError !== undefined) && <p>{uploadError}</p>}
		</form>
	</>
    );
}

export default InItemList;
