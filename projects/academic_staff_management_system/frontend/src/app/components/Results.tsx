import React from 'react'
import Card from './Card'

type Props = {}

export default function Results({}: Props) {
  return (
    <div className='lg:flex-auto'>
      <h2 className="text-main-highlight-text text-[24px] font-bold">
        Results
      </h2>
      <div className="mt-[15px] flex flex-col gap-[10px]">
        <Card />
        <Card />
        <Card />
        <Card />
      </div>
    </div>
  );
}