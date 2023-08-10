import { Outlet, Link } from 'react-router-dom';

import '../App.css';


function NavBar() {
  return (
      <nav>
        <Link to='/in-items/'>In Items</Link>
        <Link to='/projects/'>Projects</Link>
      </nav>
  )
}


const Root = () => {
  return (
    <>
      <NavBar />
      <Outlet />
    </>
  )
}


export default Root;
