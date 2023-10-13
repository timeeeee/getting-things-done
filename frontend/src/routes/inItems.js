import React, { useEffect, useRef, useState } from 'react';
import { useFetcher, useLoaderData } from 'react-router-dom';
import axios from 'axios';


export async function inItemListLoader() {
	const response = await axios.get('http://localhost:8000/in-items');
	const inItems = response.data;
	return { inItems };
}


export async function createInItemAction({ params, request }) {
	console.log("formData:");
	const formData = await request.formData();
	console.log(formData);

	const response = await axios.post(
		'http://localhost:8000/in-items', 
		Object.fromEntries(formData));

	const item = await response.data;
	return { item };
}


export async function updateInItemAction({ params, request }) {
	const formData = await request.formData();
	console.log(formData);
	
	const response = await axios.put(
		`http://localhost:8000/in-items/${formData.get("id")}`,
		{description: formData.get("description")}
	);
	const item = await response.data;
	return { item };
}


// todo: add 'is saving'
function InItem({description, id}) {
	const [isProcessing, setIsProcessing] = useState(false);

	const fetcher = useFetcher();

	useEffect(() => {
		if (fetcher.state === 'submitting') {
			setIsProcessing(false);
		}
	}, [fetcher])

	if (!isProcessing) return (
		<li className='in-item' key={id}>
			<div>{description}</div>
			<button onClick={() => setIsProcessing(true)} disabled={(fetcher.state === 'submitting')}>Process</button>
		</li>
	);

	return (
		<fetcher.Form method='post' action={`/in-items/update`} >
			<input type='text' name='description' defaultValue={description} />
			<input type='hidden' name='id' defaultValue={id} />
			<input type='button' name='delete' value='delete' />
			<input type='button' name='cancel' onClick={() => setIsProcessing(false)} value='cancel' />
			<input type='submit' />
		</fetcher.Form>
	);
}


function InItemList() {
	const { inItems } = useLoaderData();
	const fetcher = useFetcher();

	const formRef = useRef(null);
	const descriptionInputRef = useRef(null);

	useEffect(() => {
		console.log(`current state is ${fetcher.status}`);
		console.log('current data is...');
		console.log(fetcher.data);

		// load?
		if (fetcher.state === 'idle' && !fetcher.data) {
			// what does this do now that it only loads data for the form?
			fetcher.load()
		}

		const element = descriptionInputRef.current;
		if (element !== null) {
			element.scrollIntoView({ behavior: "smooth" });
			element.value = '';
			element.focus();
		}
	}, [fetcher]);

	return (
		<>
			<ul>
				{inItems.map(item => <InItem description={item.description} id={item.id} key={item.id} />)}
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
