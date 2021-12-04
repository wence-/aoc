module Main where
import Data.Foldable (foldl')

data Move = F Int | D Int
  deriving (Eq, Show)

parse :: String -> Maybe Move
parse ('f':xs) = Just . F $ read (drop 7 xs)
parse ('d':xs) = Just . D $ read (drop 4 xs)
parse ('u':xs) = Just . D $ -read (drop 2 xs)
parse _ = Nothing

inp :: String -> IO (Maybe [Move])
inp path = do
  c <- readFile path
  return $ mapM parse (lines c)

part1 :: Maybe [Move] -> Int
part1 Nothing = 0
part1 (Just xs) = h * d
  where (h, d) = foldl' (\(h, d) x ->
                           case x of
                             F n -> (h + n, d)
                             D n -> (h, d + n))
                 (0, 0) xs

part2 :: Maybe [Move] -> Int
part2 Nothing = 0
part2 (Just xs) = h * d
  where (h, d, _) = foldl' (\(h, d, a) x ->
                              case x of
                                F n -> (h + n, d + (a * n), a)
                                D n -> (h, d, a + n))
                    (0, 0, 0) xs

main :: IO ()
main = do
  instructions <- inp "../inputs/2021/day02.input"
  print $ part1 instructions
  print $ part2 instructions
