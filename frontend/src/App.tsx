import axios from 'axios';
import React, { useCallback, useEffect, useState } from 'react';
import Footer from './Footer';
import { Character, Quote, TVShow } from './types';

const DEFAULT_QUOTE: Quote = {
  quote: "What this thing needs is what we call a 'Brogan' adjustment.",
  said_by: "Paulie Gualtieri",
  season_number: 2,
  episode_number: 4,
  tv_show: "Sopranos"
}

function App() {

  const [quote, setQuote] = useState<Quote>()
  const [error, setError] = useState(false)
  const [loading, setLoading] = useState(true)

  const getRandomQuote = () => {
    axios.get<Quote>("api/quotes/random")
      .then( async ({ data }) => {

        //Grab Character Name and TV Show Name
        const details = await Promise.all([axios.get<Character>(data.said_by), axios.get<TVShow>(data.tv_show)])

        const said_by = details[0].data.name
        const tv_show = details[1].data.name

        setQuote({ ...data, said_by, tv_show })

      })
      .catch((e) => {
        setError(true)
        setQuote(DEFAULT_QUOTE)

      })
      .finally(() => setLoading(false))

  }

  useEffect(() => {
    getRandomQuote()
  }, [])

  const onButtonPress = useCallback(() => {

    if (error) {
      window.location.reload()
    }

    else {
      getRandomQuote()
    }

  }, [error])

  if (loading){
    return null
  }

  return (
    <div className="flex flex-col items-center justify-center min-h-screen px-8 gap-4">

      <div className='flex flex-col gap-4 font-serif'>
        <h1 className='text-4xl text-center'>{`"${quote?.quote}"`}</h1>
        <h2 className='self-center sm:self-end'>{`${quote?.said_by}. ${quote?.tv_show}. S${quote?.season_number}E${quote?.episode_number}`}</h2>
      </div>

      <button onClick={onButtonPress} className='border-black p-2 font-serif uppercase border-2 tracking-widest hover:bg-red-500 duration-300 hover:text-white'>{error ? "Reload" : "Random"}</button>

      <Footer/>

    </div>
  );
}

export default App;
