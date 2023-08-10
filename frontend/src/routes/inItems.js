import React, { useEffect, useRef } from 'react';
import { useFetcher } from 'react-router-dom';
import axios from 'axios';


export async function inItemListLoader() {
	const response = await axios.get('http://localhost:8000/in-items');
	const inItems = response.data;
	return { inItems };
}


export async function createInItemAction({ params, request }) {
	// clear the input

	console.log("action params:");
	console.log(params);
	console.log("action request");
	console.log(request);
	console.log("formData:");
	const formData = await request.formData();
	console.log(formData);

	const response = await axios.post(
		'http://localhost:8000/in-items', 
		Object.fromEntries(formData));

	const item = await response.data;
	return { item };
}


// todo: add 'is saving'
function InItem({description, id}) {
	return <li className='in-item' key={id}>{description}</li>;
}


function InItemList() {
	const fetcher = useFetcher();

	// const [uploadError, setUploadError] = useState();

	const formRef = useRef(null);
	const descriptionInputRef = useRef(null);

	useEffect(() => {
		console.log(`current state is ${fetcher.status}`);
		console.log('current data is...');
		console.log(fetcher.data);

		// load?
		if (fetcher.state === 'idle' && !fetcher.data) {
			console.log("calling load");
			fetcher.load()
		}

		const element = descriptionInputRef.current;
		if (element !== null) {
			element.scrollIntoView({ behavior: "smooth" });
			element.focus();
		}
	}, [fetcher]);

	/*
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
	*/

	if (fetcher.state === 'loading' || fetcher.data == undefined) return <p>loading...</p>;

	return (
		<>
			<ul>
				{fetcher.data.inItems.map(item => <InItem description={item.description} key={item.id} />)}
			</ul>
			
			<fetcher.Form method='post' action='/in-items/create' ref={formRef}>
				<h2>Add an item</h2>
				<input type='text' name='description' disabled={fetcher.state === 'submitting'} ref={descriptionInputRef} />
				<input type='submit' disabled={fetcher.state === 'submitting'} value='submit' />

				{
					// (uploadError !== undefined) && <p>{uploadError}</p>
				}
			</fetcher.Form>
		</>
	);
    

}

export default InItemList;
