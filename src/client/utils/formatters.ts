



export function formatNumber(num: number) {
    // Ensure num is a number
    num = Number(num);
    if (isNaN(num)) return "Not a number";
  
    // Format for numbers less than 1,000
    if (num < 1000) return num.toString();
  
    // Format for numbers in the thousands (1,000 - 999,999)
    if (num >= 1000 && num < 1000000) {
      return (num / 1000).toFixed(0) + 'K';
    }
  
    // Format for numbers in the millions (1,000,000 and above)
    if (num >= 1000000) {
      return (num / 1000000).toFixed(2) + 'M';
    }
}

export function formatTimestampAsTime(timestamp: number) {

	// Convert to milliseconds to create a Date object
	const date = new Date(timestamp * 1000);

	// Convert to Eastern Time
	const easternTime = date.toLocaleTimeString("en-US", { timeZone: "America/New_York", hour: '2-digit', minute: '2-digit', second: '2-digit' });

	return easternTime
}