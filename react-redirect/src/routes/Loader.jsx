import { useParams, useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import "../css/loader.css";

export default function Loader() {
  const redirect = useNavigate();
  const { id } = useParams();
  const fetchUrl = import.meta.env.VITE_FETCH_URL;

  useEffect(() => {
    const fetchData = async () => {
      try {
        const request = {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ id }),
        };

        const response = await fetch(fetchUrl, request);
        if (response.status !== 200) {
          redirect("/");
        } else {
          const data = await response.json();
          window.location.href = data["original_url"];
        }
      } catch (error) {
        redirect("/");
      }
    };

    fetchData();
  }, [fetchUrl, id, redirect]);

  return (
    <>
      <div className="loader-container">
        <span className="loader"></span>
      </div>
    </>
  );
}