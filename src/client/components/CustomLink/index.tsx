import React from 'react';
import Link from 'next/link';
import { useRouter } from 'next/router';

const GATrackingId = 'UA-XXXXXXXXX-X'; // TODO: Replace with GA Tracking ID

// Function to send a pageview to Google Analytics
const trackPageView = (url: string) => {
    //TODO: Set Up Page View Tracking for Google Analytics
    
    //   window.gtag('config', GATrackingId, {
    //     page_path: url,
    //   });
};

const isExternalLink = (url: string) => {
    // A simple check to determine if the URL is external
    return /^(http|https):\/\//.test(url);
};


// This component is to allow the use of Next's Link component to
// help with SEO, while also tracking the link clicks using 
// Google Analytics
const CustomLink = ({ href, children, ...props }: any) => {
    const router = useRouter();
  
    const handleClick = (e: any) => {
      // Prevent default if internal link to utilize Next.js navigation
      if (!isExternalLink(href)) {
        e.preventDefault();
        trackPageView(href);
        router.push(href);
      } else {
        // For external links, track the page view and let the browser navigate naturally
        trackPageView(href);
      }
    };
  
    if (isExternalLink(href)) {
      // Directly return an anchor tag for external links
      return (
        <a href={href} onClick={handleClick} target="_blank" rel="noopener noreferrer" {...props}>
          {children}
        </a>
      );
    } else {
      // Use Next.js Link for internal links
      return (
        <Link href={href} passHref>
          {React.cloneElement(React.Children.only(children), { onClick: handleClick })}
        </Link>
      );
    }
};

export default CustomLink;
