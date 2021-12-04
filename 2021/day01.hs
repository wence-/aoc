module Main where
import Data.List (tails)

inp :: String -> IO [Int]
inp path = do
  c <- readFile path
  return $ map read (lines c)

solve :: Int -> [Int] -> Int
solve n xs = sum $ zipWith ((fromEnum .) . (<)) xs (drop n xs)

main :: IO ()
main = do
  vals <- inp "../inputs/2021/day01.input"
  print $ solve 1 vals
  print $ solve 3 vals
