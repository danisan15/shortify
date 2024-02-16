import "../css/error.css";

const Error = () => {
    const homeUrl = import.meta.env.VITE_HOME_URL;

  return (
    <>
        <div className="container">
            <div id="text" className="text">
                <div className="text-404">
                    <h1>4</h1>
                    <h1>0</h1>
                    <h1>4</h1>
                </div>
                <p>Oops! Page not found</p>
                <a href={homeUrl} className="btn">Back to Home</a>
            </div>
        </div>
    </>
  )
}

export default Error